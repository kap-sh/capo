"""Generated from Smithy shape ``com.amazonaws.connectcases#GetDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.created_time
    import capo_connectcases.types.domain_arn
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.domain_name
    import capo_connectcases.types.domain_status
    import capo_connectcases.types.tags


class GetDomainResponse(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    domain_arn: "capo_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) for the Cases domain.</p>"""
    name: "capo_connectcases.types.domain_name.DomainName"
    """<p>The name of the Cases domain.</p>"""
    created_time: "capo_connectcases.types.created_time.CreatedTime"
    """<p>The timestamp when the Cases domain was created.</p>"""
    domain_status: "capo_connectcases.types.domain_status.DomainStatus"
    """<p>The status of the Cases domain.</p>"""
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainResponse) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["name"] = value["name"]
    import capo_connectcases.types.created_time

    out["createdTime"] = capo_connectcases.types.created_time.serialize_json(
        value["created_time"]
    )
    out["domainStatus"] = value["domain_status"]
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDomainResponse:
    out: GetDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createdTime") is not None:
        import capo_connectcases.types.created_time

        out["created_time"] = capo_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("domainStatus") is not None:
        out["domain_status"] = data["domainStatus"]
    else:
        out["domain_status"] = ""
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    return out
