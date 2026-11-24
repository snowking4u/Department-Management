from flask import Blueprint, render_template, session, redirect, url_for, abort, request, flash
from extensions import db
from models import Student, Faculty, Admin, Notice

hod_bp = Blueprint("hod", __name__)


def require_hod():
    """Helper to verify HOD session"""
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    if session.get("user_role", "").lower() != "hod":
        abort(403)
    return None


@hod_bp.route("/hod_dashboard")
def hod_dashboard():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    # Fetch logged-in HOD
    hod = Admin.query.get(session["user_id"])
    if not hod:
        session.clear()
        return redirect(url_for("auth.login"))

    # Dynamic counts for summary cards
    total_students = Student.query.count()
    total_faculty = Faculty.query.count()
    low_attendance_count = Student.query.filter(
        Student.attendance_percentage < 75
    ).count()

    return render_template(
        "hod_dashboard.html",
        hod=hod,
        total_students=total_students,
        total_faculty=total_faculty,
        low_attendance_count=low_attendance_count
    )


@hod_bp.route("/student-management")
def student_management():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    students = Student.query.all()
    return render_template("student_management.html", students=students)


@hod_bp.route("/faculty")
def faculty_management():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    faculty_users = Faculty.query.all()

    faculty_users_data = [
        {
            "id": user.faculty_id,
            "name": user.name,
            "email": user.email,
            "designation": user.designation,
            "qualifications": user.qualifications,
        }
        for user in faculty_users
    ]

    return render_template(
        "faculty.html",
        faculty_users=faculty_users,
        faculty_users_data=faculty_users_data
    )


# ============================================================================
# NOTICE MANAGEMENT ROUTES
# ============================================================================

@hod_bp.route("/notice-management")
def notice_management():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    q = request.args.get("q", "").strip()
    category = request.args.get("category", "All").strip()
    audience = request.args.get("audience", "All").strip()

    query = Notice.query

    if q:
        search_filter = db.or_(
            Notice.title.ilike(f"%{q}%"),
            Notice.description.ilike(f"%{q}%")
        )
        query = query.filter(search_filter)

    if category and category != "All":
        query = query.filter(Notice.category == category)

    if audience and audience != "All":
        query = query.filter(Notice.target_audience == audience)

    notices = query.order_by(Notice.is_pinned.desc(), Notice.created_at.desc()).all()

    # Dynamic counts for notice stats
    total_notices = Notice.query.count()
    active_notices = Notice.query.filter_by(is_active=True).count()
    student_notices = Notice.query.filter(Notice.target_audience.in_(["All", "Students"])).count()
    faculty_notices = Notice.query.filter(Notice.target_audience.in_(["All", "Faculty"])).count()

    return render_template(
        "notice_management.html",
        notices=notices,
        total_notices=total_notices,
        active_notices=active_notices,
        student_notices=student_notices,
        faculty_notices=faculty_notices,
        current_q=q,
        current_category=category,
        current_audience=audience
    )


@hod_bp.route("/notice-management/create", methods=["POST"])
def create_notice():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    category = request.form.get("category", "General").strip()
    target_audience = request.form.get("target_audience", "All").strip()
    is_pinned = bool(request.form.get("is_pinned"))
    attachment_url = request.form.get("attachment_url", "").strip() or None

    if not title or not description:
        flash("Title and description are required.", "error")
        return redirect(url_for("hod.notice_management"))

    new_notice = Notice(
        title=title,
        description=description,
        category=category,
        target_audience=target_audience,
        is_pinned=is_pinned,
        attachment_url=attachment_url,
        author_name=session.get("user_name", "Head of Department")
    )

    db.session.add(new_notice)
    db.session.commit()
    flash("Notice published successfully!", "success")
    return redirect(url_for("hod.notice_management"))


@hod_bp.route("/notice-management/edit/<int:notice_id>", methods=["POST"])
def edit_notice(notice_id):
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    notice = Notice.query.get_or_404(notice_id)

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    category = request.form.get("category", "General").strip()
    target_audience = request.form.get("target_audience", "All").strip()
    is_pinned = bool(request.form.get("is_pinned"))
    attachment_url = request.form.get("attachment_url", "").strip() or None

    if not title or not description:
        flash("Title and description are required.", "error")
        return redirect(url_for("hod.notice_management"))

    notice.title = title
    notice.description = description
    notice.category = category
    notice.target_audience = target_audience
    notice.is_pinned = is_pinned
    notice.attachment_url = attachment_url

    db.session.commit()
    flash("Notice updated successfully!", "success")
    return redirect(url_for("hod.notice_management"))


@hod_bp.route("/notice-management/delete/<int:notice_id>", methods=["POST"])
def delete_notice(notice_id):
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    notice = Notice.query.get_or_404(notice_id)
    db.session.delete(notice)
    db.session.commit()
    flash("Notice deleted successfully!", "success")
    return redirect(url_for("hod.notice_management"))


@hod_bp.route("/notice-management/toggle-pin/<int:notice_id>", methods=["POST"])
def toggle_pin(notice_id):
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    notice = Notice.query.get_or_404(notice_id)
    notice.is_pinned = not notice.is_pinned
    db.session.commit()
    return redirect(url_for("hod.notice_management"))


