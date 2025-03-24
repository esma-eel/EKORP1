import sqlalchemy as sa
from apps.extensions import db

from apps.groups.models import GroupMembership, UserGroup


def get_groups_object():
    objects = db.session.scalars(sa.select(UserGroup)).all()
    return objects


def get_groups_name():
    names = db.session.scalars(sa.select(UserGroup.name)).all()
    return names


def get_group_object_by_name(group_name):
    group_object = UserGroup.query.filter_by(name=group_name).first()
    return group_object


def create_membership(profile, group):
    membership = GroupMembership(profile=profile, group=group)
    db.session.add(membership)
    db.session.commit()


def remove_membership(profile, group):
    membership = GroupMembership.query.filter_by(
        profile_id=profile.id, group_id=group.id
    ).first()
    if membership:
        db.session.delete(membership)
        db.session.commit()
        return True

    return False


def add_user_to_group(profile, group_name):
    group = get_group_object_by_name(group_name)
    create_membership(profile, group)


def remove_user_from_group(profile, group_name):
    group = get_group_object_by_name(group_name)
    result = remove_membership(profile, group)
    return result


def get_users_membership(profile):
    if profile.group_memberships:
        return profile.group_memberships[0]

    return None


def get_users_current_group(profile):
    membership = get_users_membership(profile)
    if membership:
        return membership.group

    return None


def user_is_member(profile, group_name):
    group = get_group_object_by_name(group_name)
    exists = (
        GroupMembership.query.filter_by(
            profile_id=profile.id, group_id=group.id
        ).first()
        is not None
    )
    return exists
