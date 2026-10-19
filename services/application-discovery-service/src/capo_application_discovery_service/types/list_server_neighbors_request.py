"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListServerNeighborsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.boolean
    import capo_application_discovery_service.types.configuration_id
    import capo_application_discovery_service.types.configuration_id_list
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.string


class ListServerNeighborsRequest(TypedDict, closed=True):
    configuration_id: (
        "capo_application_discovery_service.types.configuration_id.ConfigurationId"
    )
    """<p>Configuration ID of the server for which neighbors are being listed.</p>"""
    port_information_needed: NotRequired[
        "capo_application_discovery_service.types.boolean.Boolean"
    ]
    """<p>Flag to indicate if port and protocol information is needed as part of the response.</p>"""
    neighbor_configuration_ids: NotRequired[
        "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    ]
    """<p>List of configuration IDs to test for one-hop-away.</p>"""
    max_results: NotRequired["capo_application_discovery_service.types.integer.Integer"]
    """<p>Maximum number of results to return in a single page of output.</p>"""
    next_token: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>Token to retrieve the next set of results. For example, if you previously specified 100 IDs for <code>ListServerNeighborsRequest$neighborConfigurationIds</code> but set <code>ListServerNeighborsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServerNeighborsRequest) -> dict:
    out: dict = {}
    out["configurationId"] = value["configuration_id"]
    if "port_information_needed" in value:
        out["portInformationNeeded"] = value["port_information_needed"]
    if "neighbor_configuration_ids" in value:
        import capo_application_discovery_service.types.configuration_id_list

        out["neighborConfigurationIds"] = (
            capo_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
                value["neighbor_configuration_ids"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServerNeighborsRequest:
    out: ListServerNeighborsRequest = {}  # type: ignore[typeddict-item]
    if data.get("configurationId") is not None:
        out["configuration_id"] = data["configurationId"]
    else:
        out["configuration_id"] = ""
    if data.get("portInformationNeeded") is not None:
        out["port_information_needed"] = data["portInformationNeeded"]
    if data.get("neighborConfigurationIds") is not None:
        import capo_application_discovery_service.types.configuration_id_list

        out["neighbor_configuration_ids"] = (
            capo_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["neighborConfigurationIds"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
