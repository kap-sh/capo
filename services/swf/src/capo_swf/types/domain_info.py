"""Generated from Smithy shape ``com.amazonaws.swf#DomainInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.arn
    import capo_swf.types.description
    import capo_swf.types.domain_name
    import capo_swf.types.registration_status


class DomainInfo(TypedDict, closed=True):
    name: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain. This name is unique within the account.</p>"""
    status: "capo_swf.types.registration_status.RegistrationStatus"
    """<p>The status of the domain:</p> <ul> <li> <p> <code>REGISTERED</code> – The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions. </p> </li> <li> <p> <code>DEPRECATED</code> – The domain was deprecated using <a>DeprecateDomain</a>, but is still in use. You should not create new workflow executions in this domain. </p> </li> </ul>"""
    description: NotRequired["capo_swf.types.description.Description"]
    """<p>The description of the domain provided through <a>RegisterDomain</a>.</p>"""
    arn: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The ARN of the domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainInfo) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_swf.types.registration_status

    out["status"] = capo_swf.types.registration_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainInfo:
    out: DomainInfo = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_swf.types.registration_status

        out["status"] = capo_swf.types.registration_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_swf.types.registration_status.RegistrationStatus", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
