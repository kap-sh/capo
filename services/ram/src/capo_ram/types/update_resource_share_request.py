"""Generated from Smithy shape ``com.amazonaws.ram#UpdateResourceShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.boolean
    import capo_ram.types.string


class UpdateResourceShareRequest(TypedDict, closed=True):
    resource_share_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to modify.</p>"""
    name: NotRequired["capo_ram.types.string.String"]
    """<p>If specified, the new name that you want to attach to the resource share.</p>"""
    allow_external_principals: NotRequired["capo_ram.types.boolean.Boolean"]
    """<p>Specifies whether principals outside your organization in Organizations can be associated with a resource share.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceShareRequest) -> dict:
    out: dict = {}
    out["resourceShareArn"] = value["resource_share_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "allow_external_principals" in value:
        out["allowExternalPrincipals"] = value["allow_external_principals"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateResourceShareRequest:
    out: UpdateResourceShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    else:
        raise DeserializationError(
            "UpdateResourceShareRequest.resource_share_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("allowExternalPrincipals") is not None:
        out["allow_external_principals"] = data["allowExternalPrincipals"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
