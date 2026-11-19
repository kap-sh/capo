"""Generated from Smithy shape ``com.amazonaws.snowball#ServiceVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class ServiceVersion(TypedDict, closed=True):
    version: NotRequired["capo_snowball.types.string.String"]
    """<p>The version number of the requested service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceVersion:
    out: ServiceVersion = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_cbor(data: dict) -> ServiceVersion:
    out: ServiceVersion = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
