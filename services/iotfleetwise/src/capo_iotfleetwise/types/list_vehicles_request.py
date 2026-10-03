"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListVehiclesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.attribute_names_list
    import capo_iotfleetwise.types.attribute_values_list
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.list_vehicles_max_results
    import capo_iotfleetwise.types.next_token


class ListVehiclesRequest(TypedDict, closed=True):
    model_manifest_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p> The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model. </p>"""
    attribute_names: NotRequired[
        "capo_iotfleetwise.types.attribute_names_list.attributeNamesList"
    ]
    """<p>The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, <code>attributeNames</code> could be "<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>" and the corresponding <code>attributeValues</code> could be "<code>1.3 L R2, Blue</code>" . In this case, the API will filter vehicles with an attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of "<code>Blue</code>". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filters to return the subset of vehicles that match the attributes filter condition.</p>"""
    attribute_values: NotRequired[
        "capo_iotfleetwise.types.attribute_values_list.attributeValuesList"
    ]
    """<p>Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with <code>attributeNames</code> to list the vehicles containing all the <code>attributeValues</code> corresponding to the <code>attributeNames</code> filter. For example, <code>attributeValues</code> could be "<code>1.3 L R2, Blue</code>" and the corresponding <code>attributeNames</code> filter could be "<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>". In this case, the API will filter vehicles with attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of "<code>Blue</code>". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filter to return the subset of vehicles that match the attributes filter condition.</p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired[
        "capo_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
    ]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVehiclesRequest) -> dict:
    out: dict = {}
    if "model_manifest_arn" in value:
        out["modelManifestArn"] = value["model_manifest_arn"]
    if "attribute_names" in value:
        import capo_iotfleetwise.types.attribute_names_list

        out["attributeNames"] = (
            capo_iotfleetwise.types.attribute_names_list.serialize_aws_json_1_0(
                value["attribute_names"]
            )
        )
    if "attribute_values" in value:
        import capo_iotfleetwise.types.attribute_values_list

        out["attributeValues"] = (
            capo_iotfleetwise.types.attribute_values_list.serialize_aws_json_1_0(
                value["attribute_values"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "list_response_scope" in value:
        import capo_iotfleetwise.types.list_response_scope

        out["listResponseScope"] = (
            capo_iotfleetwise.types.list_response_scope.serialize_aws_json_1_0(
                value["list_response_scope"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVehiclesRequest:
    out: ListVehiclesRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    if data.get("attributeNames") is not None:
        import capo_iotfleetwise.types.attribute_names_list

        out["attribute_names"] = (
            capo_iotfleetwise.types.attribute_names_list.deserialize_aws_json_1_0(
                data["attributeNames"]
            )
        )
    if data.get("attributeValues") is not None:
        import capo_iotfleetwise.types.attribute_values_list

        out["attribute_values"] = (
            capo_iotfleetwise.types.attribute_values_list.deserialize_aws_json_1_0(
                data["attributeValues"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("listResponseScope") is not None:
        import capo_iotfleetwise.types.list_response_scope

        out["list_response_scope"] = (
            capo_iotfleetwise.types.list_response_scope.deserialize_aws_json_1_0(
                data["listResponseScope"]
            )
        )
    return out
