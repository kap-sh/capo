"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeTimeSeriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.property_data_type
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.workspace_name


class DescribeTimeSeriesResponse(TypedDict, closed=True):
    asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset in which the asset property was created.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    alias: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the time series.</p>"""
    time_series_id: "capo_iotsitewise.types.time_series_id.TimeSeriesId"
    """<p>The ID of the time series.</p>"""
    data_type: "capo_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the time series.</p> <p>If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this time series.</p>"""
    data_type_spec: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this time series. This parameter is required for time series that have the <code>STRUCT</code> data type.</p> <p>The options for this parameter depend on the type of the composite model in which you created the asset property that is associated with your time series. Use <code>AWS/ALARM_STATE</code> for alarm state in alarm composite models.</p>"""
    time_series_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date that the time series was created, in Unix epoch time.</p>"""
    time_series_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date that the time series was last updated, in Unix epoch time.</p>"""
    time_series_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the time series, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId}</code> </p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTimeSeriesResponse) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types.property_data_type

    out["dataType"] = capo_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "data_type_spec" in value:
        out["dataTypeSpec"] = value["data_type_spec"]
    import capo_iotsitewise.types.timestamp

    out["timeSeriesCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["time_series_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["timeSeriesLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["time_series_last_update_date"]
    )
    out["timeSeriesArn"] = value["time_series_arn"]
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> DescribeTimeSeriesResponse:
    out: DescribeTimeSeriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    else:
        raise DeserializationError("DescribeTimeSeriesResponse.time_series_id required")
    if data.get("dataType") is not None:
        import capo_iotsitewise.types.property_data_type

        out["data_type"] = capo_iotsitewise.types.property_data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("DescribeTimeSeriesResponse.data_type required")
    if data.get("dataTypeSpec") is not None:
        out["data_type_spec"] = data["dataTypeSpec"]
    if data.get("timeSeriesCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["time_series_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["timeSeriesCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTimeSeriesResponse.time_series_creation_date required"
        )
    if data.get("timeSeriesLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["time_series_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["timeSeriesLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTimeSeriesResponse.time_series_last_update_date required"
        )
    if data.get("timeSeriesArn") is not None:
        out["time_series_arn"] = data["timeSeriesArn"]
    else:
        raise DeserializationError(
            "DescribeTimeSeriesResponse.time_series_arn required"
        )
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    return out
