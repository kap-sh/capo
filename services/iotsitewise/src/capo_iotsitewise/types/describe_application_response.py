"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.application_description
    import capo_iotsitewise.types.application_id
    import capo_iotsitewise.types.application_name
    import capo_iotsitewise.types.application_status
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dns_subdomain
    import capo_iotsitewise.types.workspace_name


class DescribeApplicationResponse(TypedDict, closed=True):
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>ARN of the application</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the application was created</p>"""
    dns_subdomain: "capo_iotsitewise.types.dns_subdomain.DnsSubdomain"
    """<p>DNS subdomain for the application</p>"""
    description: NotRequired[
        "capo_iotsitewise.types.application_description.ApplicationDescription"
    ]
    """<p>Description of the application</p>"""
    id: "capo_iotsitewise.types.application_id.ApplicationId"
    """<p>Unique identifier of the application</p>"""
    idc_application_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>Identity Center Application ARN associated with this application</p>"""
    name: "capo_iotsitewise.types.application_name.ApplicationName"
    """<p>Name of the application</p>"""
    status: "capo_iotsitewise.types.application_status.ApplicationStatus"
    """<p>Current status of the application</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when the application was last updated</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>Name of the workspace this application belongs to</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_iotsitewise.types._prelude.timestamp

    out["createdAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["dnsSubdomain"] = value["dns_subdomain"]
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["idcApplicationArn"] = value["idc_application_arn"]
    out["name"] = value["name"]
    import capo_iotsitewise.types.application_status

    out["status"] = capo_iotsitewise.types.application_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types._prelude.timestamp

    out["updatedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> DescribeApplicationResponse:
    out: DescribeApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["created_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("dnsSubdomain") is not None:
        out["dns_subdomain"] = data["dnsSubdomain"]
    else:
        out["dns_subdomain"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("idcApplicationArn") is not None:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        out["idc_application_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.application_status

        out["status"] = capo_iotsitewise.types.application_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.application_status.ApplicationStatus", ""
        )
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["updated_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    return out
