"""Generated from Smithy shape ``com.amazonaws.gamelift#FilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_list


class FilterConfiguration(TypedDict, closed=True):
    allowed_locations: NotRequired["capo_gamelift.types.location_list.LocationList"]
    """<p> A list of locations to allow game session placement in, in the form of Amazon Web Services Region codes such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterConfiguration) -> dict:
    out: dict = {}
    if "allowed_locations" in value:
        import capo_gamelift.types.location_list

        out["AllowedLocations"] = (
            capo_gamelift.types.location_list.serialize_aws_json_1_1(
                value["allowed_locations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedLocations") is not None:
        import capo_gamelift.types.location_list

        out["allowed_locations"] = (
            capo_gamelift.types.location_list.deserialize_aws_json_1_1(
                data["AllowedLocations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterConfiguration) -> dict:
    out: dict = {}
    if "allowed_locations" in value:
        import capo_gamelift.types.location_list

        out["AllowedLocations"] = capo_gamelift.types.location_list.serialize_cbor(
            value["allowed_locations"]
        )
    return out


def deserialize_cbor(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedLocations") is not None:
        import capo_gamelift.types.location_list

        out["allowed_locations"] = capo_gamelift.types.location_list.deserialize_cbor(
            data["AllowedLocations"]
        )
    return out
