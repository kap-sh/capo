"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryDistributeOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_distribute_output_configuration_locations


class ProtectedQueryDistributeOutputConfiguration(TypedDict, closed=True):
    locations: "capo_cleanrooms.types.protected_query_distribute_output_configuration_locations.ProtectedQueryDistributeOutputConfigurationLocations"
    """<p> A list of locations where you want to distribute the protected query results. Each location must specify either an S3 destination or a collaboration member destination.</p> <important> <p>You can't specify more than one S3 location.</p> <p>You can't specify the query runner's account as a member location.</p> <p>You must include either an S3 or member output configuration for each location, but not both.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryDistributeOutputConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_query_distribute_output_configuration_locations

    out["locations"] = (
        capo_cleanrooms.types.protected_query_distribute_output_configuration_locations.serialize_json(
            value["locations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryDistributeOutputConfiguration:
    out: ProtectedQueryDistributeOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("locations") is not None:
        import capo_cleanrooms.types.protected_query_distribute_output_configuration_locations

        out["locations"] = (
            capo_cleanrooms.types.protected_query_distribute_output_configuration_locations.deserialize_json(
                data["locations"]
            )
        )
    else:
        out["locations"] = []
    return out
