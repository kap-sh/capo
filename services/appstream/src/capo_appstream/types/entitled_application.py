"""Generated from Smithy shape ``com.amazonaws.appstream#EntitledApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class EntitledApplication(TypedDict, closed=True):
    application_identifier: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitledApplication) -> dict:
    out: dict = {}
    if "application_identifier" in value:
        out["ApplicationIdentifier"] = value["application_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitledApplication:
    out: EntitledApplication = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitledApplication) -> dict:
    out: dict = {}
    if "application_identifier" in value:
        out["ApplicationIdentifier"] = value["application_identifier"]
    return out


def deserialize_cbor(data: dict) -> EntitledApplication:
    out: EntitledApplication = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    return out
