"""Generated from Smithy shape ``com.amazonaws.appstream#CreateFleetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.fleet


class CreateFleetResult(TypedDict, closed=True):
    fleet: NotRequired["capo_appstream.types.fleet.Fleet"]
    """<p>Information about the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetResult) -> dict:
    out: dict = {}
    if "fleet" in value:
        import capo_appstream.types.fleet

        out["Fleet"] = capo_appstream.types.fleet.serialize_aws_json_1_1(value["fleet"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetResult:
    out: CreateFleetResult = {}  # type: ignore[typeddict-item]
    if data.get("Fleet") is not None:
        import capo_appstream.types.fleet

        out["fleet"] = capo_appstream.types.fleet.deserialize_aws_json_1_1(
            data["Fleet"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateFleetResult) -> dict:
    out: dict = {}
    if "fleet" in value:
        import capo_appstream.types.fleet

        out["Fleet"] = capo_appstream.types.fleet.serialize_cbor(value["fleet"])
    return out


def deserialize_cbor(data: dict) -> CreateFleetResult:
    out: CreateFleetResult = {}  # type: ignore[typeddict-item]
    if data.get("Fleet") is not None:
        import capo_appstream.types.fleet

        out["fleet"] = capo_appstream.types.fleet.deserialize_cbor(data["Fleet"])
    return out
