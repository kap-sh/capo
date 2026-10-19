"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateRelationalDatabaseParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_parameter_list
    import capo_lightsail.types.resource_name


class UpdateRelationalDatabaseParametersRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database for which to update parameters.</p>"""
    parameters: "capo_lightsail.types.relational_database_parameter_list.RelationalDatabaseParameterList"
    """<p>The database parameters to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRelationalDatabaseParametersRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    import capo_lightsail.types.relational_database_parameter_list

    out["parameters"] = (
        capo_lightsail.types.relational_database_parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRelationalDatabaseParametersRequest:
    out: UpdateRelationalDatabaseParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("parameters") is not None:
        import capo_lightsail.types.relational_database_parameter_list

        out["parameters"] = (
            capo_lightsail.types.relational_database_parameter_list.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = []
    return out
