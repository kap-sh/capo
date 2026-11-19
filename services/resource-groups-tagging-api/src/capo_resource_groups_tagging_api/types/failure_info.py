"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#FailureInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.error_code
    import capo_resource_groups_tagging_api.types.error_message
    import capo_resource_groups_tagging_api.types.status_code


class FailureInfo(TypedDict, closed=True):
    status_code: "capo_resource_groups_tagging_api.types.status_code.StatusCode"
    """<p>The HTTP status code of the common error.</p>"""
    error_code: NotRequired[
        "capo_resource_groups_tagging_api.types.error_code.ErrorCode"
    ]
    """<p>The code of the common error. Valid values include <code>InternalServiceException</code>, <code>InvalidParameterException</code>, and any valid error code returned by the Amazon Web Services service that hosts the resource that you want to tag.</p>"""
    error_message: NotRequired[
        "capo_resource_groups_tagging_api.types.error_message.ErrorMessage"
    ]
    """<p>The message of the common error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureInfo) -> dict:
    out: dict = {}
    out["StatusCode"] = value.get("status_code", 0)
    if "error_code" in value:
        import capo_resource_groups_tagging_api.types.error_code

        out["ErrorCode"] = (
            capo_resource_groups_tagging_api.types.error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureInfo:
    out: FailureInfo = {}  # type: ignore[typeddict-item]
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    if data.get("ErrorCode") is not None:
        import capo_resource_groups_tagging_api.types.error_code

        out["error_code"] = (
            capo_resource_groups_tagging_api.types.error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailureInfo) -> dict:
    out: dict = {}
    out["StatusCode"] = value.get("status_code", 0)
    if "error_code" in value:
        import capo_resource_groups_tagging_api.types.error_code

        out["ErrorCode"] = (
            capo_resource_groups_tagging_api.types.error_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> FailureInfo:
    out: FailureInfo = {}  # type: ignore[typeddict-item]
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    if data.get("ErrorCode") is not None:
        import capo_resource_groups_tagging_api.types.error_code

        out["error_code"] = (
            capo_resource_groups_tagging_api.types.error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
