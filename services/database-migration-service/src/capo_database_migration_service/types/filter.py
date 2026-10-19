"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_value_list
    import capo_database_migration_service.types.string


class Filter(TypedDict, closed=True):
    name: "capo_database_migration_service.types.string.String"
    """<p>The name of the filter as specified for a <code>Describe*</code> or similar operation.</p>"""
    values: "capo_database_migration_service.types.filter_value_list.FilterValueList"
    """<p>The filter value, which can specify one or more values used to narrow the returned results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_database_migration_service.types.filter_value_list

    out["Values"] = (
        capo_database_migration_service.types.filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_database_migration_service.types.filter_value_list

        out["values"] = (
            capo_database_migration_service.types.filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
