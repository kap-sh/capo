"""Generated from Smithy shape ``com.amazonaws.glue#UpdateIcebergTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_table_update_list


class UpdateIcebergTableInput(TypedDict, closed=True):
    updates: "capo_glue.types.iceberg_table_update_list.IcebergTableUpdateList"
    """<p>The list of table update operations that specify the changes to be made to the Iceberg table, including schema modifications, partition specifications, and table properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIcebergTableInput) -> dict:
    out: dict = {}
    import capo_glue.types.iceberg_table_update_list

    out["Updates"] = capo_glue.types.iceberg_table_update_list.serialize_aws_json_1_1(
        value["updates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIcebergTableInput:
    out: UpdateIcebergTableInput = {}  # type: ignore[typeddict-item]
    if data.get("Updates") is not None:
        import capo_glue.types.iceberg_table_update_list

        out["updates"] = (
            capo_glue.types.iceberg_table_update_list.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        out["updates"] = []
    return out
