"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDescribeUserLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.batch_describe_user_limits_error_list
    import capo_quicksight.types.user_limits_list


class BatchDescribeUserLimitsResponse(TypedDict, closed=True):
    user_limits: "capo_quicksight.types.user_limits_list.UserLimitsList"
    """<p>A list of user limits results. Each entry contains the effective limits for a user.</p>"""
    errors: "capo_quicksight.types.batch_describe_user_limits_error_list.BatchDescribeUserLimitsErrorList"
    """<p>A list of errors for users whose limits could not be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeUserLimitsResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.user_limits_list

    out["userLimits"] = capo_quicksight.types.user_limits_list.serialize_json(
        value["user_limits"]
    )
    import capo_quicksight.types.batch_describe_user_limits_error_list

    out["errors"] = (
        capo_quicksight.types.batch_describe_user_limits_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDescribeUserLimitsResponse:
    out: BatchDescribeUserLimitsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userLimits") is not None:
        import capo_quicksight.types.user_limits_list

        out["user_limits"] = capo_quicksight.types.user_limits_list.deserialize_json(
            data["userLimits"]
        )
    else:
        out["user_limits"] = []
    if data.get("errors") is not None:
        import capo_quicksight.types.batch_describe_user_limits_error_list

        out["errors"] = (
            capo_quicksight.types.batch_describe_user_limits_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
