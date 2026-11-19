"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.scope_name
    import capo_compute_optimizer.types.scope_value


class Scope(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.scope_name.ScopeName"]
    """<p>The name of the scope.</p> <p>The following scopes are possible:</p> <ul> <li> <p> <code>Organization</code> - Specifies that the recommendation preference applies at the organization level, for all member accounts of an organization.</p> </li> <li> <p> <code>AccountId</code> - Specifies that the recommendation preference applies at the account level, for all resources of a given resource type in an account.</p> </li> <li> <p> <code>ResourceArn</code> - Specifies that the recommendation preference applies at the individual resource level.</p> </li> </ul>"""
    value: NotRequired["capo_compute_optimizer.types.scope_value.ScopeValue"]
    """<p>The value of the scope.</p> <p>If you specified the <code>name</code> of the scope as:</p> <ul> <li> <p> <code>Organization</code> - The <code>value</code> must be <code>ALL_ACCOUNTS</code>.</p> </li> <li> <p> <code>AccountId</code> - The <code>value</code> must be a 12-digit Amazon Web Services account ID.</p> </li> <li> <p> <code>ResourceArn</code> - The <code>value</code> must be the Amazon Resource Name (ARN) of an EC2 instance or an Auto Scaling group.</p> </li> </ul> <p>Only EC2 instance and Auto Scaling group ARNs are currently supported.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Scope) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.scope_name

        out["name"] = capo_compute_optimizer.types.scope_name.serialize_aws_json_1_0(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.scope_name

        out["name"] = capo_compute_optimizer.types.scope_name.deserialize_aws_json_1_0(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Scope) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.scope_name

        out["name"] = capo_compute_optimizer.types.scope_name.serialize_cbor(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.scope_name

        out["name"] = capo_compute_optimizer.types.scope_name.deserialize_cbor(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
