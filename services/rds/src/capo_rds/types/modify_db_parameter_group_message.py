"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.parameters_list
    import capo_rds.types.string


class ModifyDBParameterGroupMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing <code>DBParameterGroup</code>.</p> </li> </ul>"""
    parameters: NotRequired["capo_rds.types.parameters_list.ParametersList"]
    """<p>An array of parameter names, values, and the application methods for the parameter update. At least one parameter name, value, and application method must be supplied; later arguments are optional. A maximum of 20 parameters can be modified in a single request.</p> <p>Valid Values (for the application method): <code>immediate | pending-reboot</code> </p> <p>You can use the <code>immediate</code> value with dynamic parameters only. You can use the <code>pending-reboot</code> value for both dynamic and static parameters.</p> <p>When the application method is <code>immediate</code>, changes to dynamic parameters are applied immediately to the DB instances associated with the parameter group.</p> <p>When the application method is <code>pending-reboot</code>, changes to dynamic and static parameters are applied after a reboot without failover to the DB instances associated with the parameter group.</p> <note> <p>You can't use <code>pending-reboot</code> with dynamic parameters on RDS for SQL Server DB instances. Use <code>immediate</code>.</p> </note> <p>For more information on modifying DB parameters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html">Working with DB parameter groups</a> in the <i>Amazon RDS User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "parameters" in value:
        import capo_rds.types.parameters_list

        capo_rds.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )


def deserialize_query(el: Element) -> ModifyDBParameterGroupMessage:
    out: ModifyDBParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_rds.types.parameters_list

        out["parameters"] = capo_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
