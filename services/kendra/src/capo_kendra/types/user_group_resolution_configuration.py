"""Generated from Smithy shape ``com.amazonaws.kendra#UserGroupResolutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.user_group_resolution_mode


class UserGroupResolutionConfiguration(TypedDict, closed=True):
    user_group_resolution_mode: (
        "capo_kendra.types.user_group_resolution_mode.UserGroupResolutionMode"
    )
    """<p>The identity store provider (mode) you want to use to get users and groups. IAM Identity Center is currently the only available mode. Your users and groups must exist in an IAM Identity Center identity source in order to use this mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserGroupResolutionConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.user_group_resolution_mode

    out["UserGroupResolutionMode"] = (
        capo_kendra.types.user_group_resolution_mode.serialize_aws_json_1_1(
            value["user_group_resolution_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserGroupResolutionConfiguration:
    out: UserGroupResolutionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("UserGroupResolutionMode") is not None:
        import capo_kendra.types.user_group_resolution_mode

        out["user_group_resolution_mode"] = (
            capo_kendra.types.user_group_resolution_mode.deserialize_aws_json_1_1(
                data["UserGroupResolutionMode"]
            )
        )
    else:
        import typing

        out["user_group_resolution_mode"] = typing.cast(
            "capo_kendra.types.user_group_resolution_mode.UserGroupResolutionMode", ""
        )
    return out
