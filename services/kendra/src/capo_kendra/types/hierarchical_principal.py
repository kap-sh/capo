"""Generated from Smithy shape ``com.amazonaws.kendra#HierarchicalPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.principal_list


class HierarchicalPrincipal(TypedDict, closed=True):
    principal_list: "capo_kendra.types.principal_list.PrincipalList"
    """<p>A list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to. Each hierarchical list specifies which user or group has allow or deny access for each document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HierarchicalPrincipal) -> dict:
    out: dict = {}
    import capo_kendra.types.principal_list

    out["PrincipalList"] = capo_kendra.types.principal_list.serialize_aws_json_1_1(
        value["principal_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HierarchicalPrincipal:
    out: HierarchicalPrincipal = {}  # type: ignore[typeddict-item]
    if data.get("PrincipalList") is not None:
        import capo_kendra.types.principal_list

        out["principal_list"] = (
            capo_kendra.types.principal_list.deserialize_aws_json_1_1(
                data["PrincipalList"]
            )
        )
    else:
        raise DeserializationError("HierarchicalPrincipal.principal_list required")
    return out
