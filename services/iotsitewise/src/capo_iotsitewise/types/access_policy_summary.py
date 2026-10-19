"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AccessPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.identity
    import capo_iotsitewise.types.permission
    import capo_iotsitewise.types.resource
    import capo_iotsitewise.types.timestamp


class AccessPolicySummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    identity: "capo_iotsitewise.types.identity.Identity"
    """<p>The identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user).</p>"""
    resource: "capo_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource (a portal or project).</p>"""
    permission: "capo_iotsitewise.types.permission.Permission"
    """<p>The permissions for the access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    creation_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the access policy was created, in Unix epoch time.</p>"""
    last_update_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the access policy was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPolicySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_iotsitewise.types.identity

    out["identity"] = capo_iotsitewise.types.identity.serialize_json(value["identity"])
    import capo_iotsitewise.types.resource

    out["resource"] = capo_iotsitewise.types.resource.serialize_json(value["resource"])
    import capo_iotsitewise.types.permission

    out["permission"] = capo_iotsitewise.types.permission.serialize_json(
        value["permission"]
    )
    if "creation_date" in value:
        import capo_iotsitewise.types.timestamp

        out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import capo_iotsitewise.types.timestamp

        out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["last_update_date"]
        )
    return out


def deserialize_json(data: dict) -> AccessPolicySummary:
    out: AccessPolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("identity") is not None:
        import capo_iotsitewise.types.identity

        out["identity"] = capo_iotsitewise.types.identity.deserialize_json(
            data["identity"]
        )
    else:
        raise DeserializationError("AccessPolicySummary.identity required")
    if data.get("resource") is not None:
        import capo_iotsitewise.types.resource

        out["resource"] = capo_iotsitewise.types.resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("AccessPolicySummary.resource required")
    if data.get("permission") is not None:
        import capo_iotsitewise.types.permission

        out["permission"] = capo_iotsitewise.types.permission.deserialize_json(
            data["permission"]
        )
    else:
        import typing

        out["permission"] = typing.cast(
            "capo_iotsitewise.types.permission.Permission", ""
        )
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    return out
