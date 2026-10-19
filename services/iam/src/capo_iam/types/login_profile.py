"""Generated from Smithy shape ``com.amazonaws.iam#LoginProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.user_name_type


class LoginProfile(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the user, which can be used for signing in to the Amazon Web Services Management Console.</p>"""
    create_date: "capo_iam.types.date_type.dateType"
    """<p>The date when the password for the user was created.</p>"""
    password_reset_required: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the user is required to set a new password on next sign-in.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoginProfile, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{key_prefix}CreateDate"
    )
    pairs.append(
        (
            f"{key_prefix}PasswordResetRequired",
            "true" if value.get("password_reset_required", False) else "false",
        )
    )


def deserialize_query(el: Element) -> LoginProfile:
    out: LoginProfile = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        import datetime

        out["create_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_password_reset_required = el.find("PasswordResetRequired")
    if child_password_reset_required is not None:
        out["password_reset_required"] = (
            child_password_reset_required.text or ""
        ).lower() == "true"
    else:
        out["password_reset_required"] = False
    return out
