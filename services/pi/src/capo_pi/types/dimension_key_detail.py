"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.detail_status
    import capo_pi.types.string


class DimensionKeyDetail(TypedDict, closed=True):
    value: NotRequired["capo_pi.types.string.String"]
    """<p>The value of the dimension detail data. Depending on the return status, this value is either the full or truncated SQL query for the following dimensions:</p> <ul> <li> <p> <code>db.query.statement</code> (Amazon DocumentDB)</p> </li> <li> <p> <code>db.sql.statement</code> (Amazon RDS and Aurora)</p> </li> </ul>"""
    dimension: NotRequired["capo_pi.types.string.String"]
    """<p>The full name of the dimension. The full name includes the group name and key name. The following values are valid:</p> <ul> <li> <p> <code>db.query.statement</code> (Amazon DocumentDB)</p> </li> <li> <p> <code>db.sql.statement</code> (Amazon RDS and Aurora)</p> </li> </ul>"""
    status: NotRequired["capo_pi.types.detail_status.DetailStatus"]
    """<p>The status of the dimension detail data. Possible values include the following:</p> <ul> <li> <p> <code>AVAILABLE</code> - The dimension detail data is ready to be retrieved.</p> </li> <li> <p> <code>PROCESSING</code> - The dimension detail data isn't ready to be retrieved because more processing time is required. If the requested detail data has the status <code>PROCESSING</code>, Performance Insights returns the truncated query.</p> </li> <li> <p> <code>UNAVAILABLE</code> - The dimension detail data could not be collected successfully.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDetail) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "status" in value:
        import capo_pi.types.detail_status

        out["Status"] = capo_pi.types.detail_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionKeyDetail:
    out: DimensionKeyDetail = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    if data.get("Status") is not None:
        import capo_pi.types.detail_status

        out["status"] = capo_pi.types.detail_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionKeyDetail) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "status" in value:
        import capo_pi.types.detail_status

        out["Status"] = capo_pi.types.detail_status.serialize_cbor(value["status"])
    return out


def deserialize_cbor(data: dict) -> DimensionKeyDetail:
    out: DimensionKeyDetail = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    if data.get("Status") is not None:
        import capo_pi.types.detail_status

        out["status"] = capo_pi.types.detail_status.deserialize_cbor(data["Status"])
    return out
