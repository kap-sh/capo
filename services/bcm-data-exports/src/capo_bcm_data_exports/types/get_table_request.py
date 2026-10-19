"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.table_name
    import capo_bcm_data_exports.types.table_properties


class GetTableRequest(TypedDict, closed=True):
    table_name: "capo_bcm_data_exports.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    table_properties: NotRequired[
        "capo_bcm_data_exports.types.table_properties.TableProperties"
    ]
    """<p>TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableRequest) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "table_properties" in value:
        import capo_bcm_data_exports.types.table_properties

        out["TableProperties"] = (
            capo_bcm_data_exports.types.table_properties.serialize_aws_json_1_1(
                value["table_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableRequest:
    out: GetTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("TableProperties") is not None:
        import capo_bcm_data_exports.types.table_properties

        out["table_properties"] = (
            capo_bcm_data_exports.types.table_properties.deserialize_aws_json_1_1(
                data["TableProperties"]
            )
        )
    return out
