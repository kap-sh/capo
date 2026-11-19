"""Generated from Smithy shape ``com.amazonaws.codedeploy#UpdateApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name


class UpdateApplicationInput(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The current name of the application you want to change.</p>"""
    new_application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The new name to give the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationInput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "new_application_name" in value:
        out["newApplicationName"] = value["new_application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationInput:
    out: UpdateApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("newApplicationName") is not None:
        out["new_application_name"] = data["newApplicationName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateApplicationInput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "new_application_name" in value:
        out["newApplicationName"] = value["new_application_name"]
    return out


def deserialize_cbor(data: dict) -> UpdateApplicationInput:
    out: UpdateApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("newApplicationName") is not None:
        out["new_application_name"] = data["newApplicationName"]
    return out
