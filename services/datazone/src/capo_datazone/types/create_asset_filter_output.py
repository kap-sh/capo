"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetFilterOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_filter_configuration
    import capo_datazone.types.asset_id
    import capo_datazone.types.column_name_list
    import capo_datazone.types.created_at
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.filter_id
    import capo_datazone.types.filter_name
    import capo_datazone.types.filter_status


class CreateAssetFilterOutput(TypedDict, closed=True):
    id: "capo_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the asset filter is created.</p>"""
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The ID of the asset.</p>"""
    name: "capo_datazone.types.filter_name.FilterName"
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    status: NotRequired["capo_datazone.types.filter_status.FilterStatus"]
    """<p>The status of the asset filter.</p>"""
    configuration: (
        "capo_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    )
    """<p>The configuration of the asset filter.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset filter was created.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message that is displayed if the asset filter is not created successfully.</p>"""
    effective_column_names: NotRequired[
        "capo_datazone.types.column_name_list.ColumnNameList"
    ]
    """<p>The column names in the asset filter.</p>"""
    effective_row_filter: NotRequired["str"]
    """<p>The row filter in the asset filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFilterOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.filter_status

        out["status"] = capo_datazone.types.filter_status.serialize_json(
            value["status"]
        )
    import capo_datazone.types.asset_filter_configuration

    out["configuration"] = (
        capo_datazone.types.asset_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "effective_column_names" in value:
        import capo_datazone.types.column_name_list

        out["effectiveColumnNames"] = (
            capo_datazone.types.column_name_list.serialize_json(
                value["effective_column_names"]
            )
        )
    if "effective_row_filter" in value:
        out["effectiveRowFilter"] = value["effective_row_filter"]
    return out


def deserialize_json(data: dict) -> CreateAssetFilterOutput:
    out: CreateAssetFilterOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.filter_status

        out["status"] = capo_datazone.types.filter_status.deserialize_json(
            data["status"]
        )
    if data.get("configuration") is not None:
        import capo_datazone.types.asset_filter_configuration

        out["configuration"] = (
            capo_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_datazone.types._unknown

        out["configuration"] = capo_datazone.types._unknown.UnknownUnionMember("")
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("effectiveColumnNames") is not None:
        import capo_datazone.types.column_name_list

        out["effective_column_names"] = (
            capo_datazone.types.column_name_list.deserialize_json(
                data["effectiveColumnNames"]
            )
        )
    if data.get("effectiveRowFilter") is not None:
        out["effective_row_filter"] = data["effectiveRowFilter"]
    return out


def redact_sensitive(value: CreateAssetFilterOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
