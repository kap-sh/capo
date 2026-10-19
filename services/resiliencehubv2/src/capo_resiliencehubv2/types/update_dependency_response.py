"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateDependencyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.uuid


class UpdateDependencyResponse(TypedDict, closed=True):
    dependency_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the updated dependency.</p>"""
    dependency_name: "str"
    """<p>The name of the updated dependency.</p>"""
    location: "str"
    """<p>The location of the dependency.</p>"""
    criticality: (
        "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
    )
    """<p>The criticality level of the dependency.</p>"""
    comment: NotRequired["str"]
    """<p>The comment about the dependency.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the dependency.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the dependency was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDependencyResponse) -> dict:
    out: dict = {}
    out["dependencyId"] = value["dependency_id"]
    out["dependencyName"] = value["dependency_name"]
    out["location"] = value["location"]
    import capo_resiliencehubv2.types.dependency_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.dependency_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "provider" in value:
        out["provider"] = value["provider"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDependencyResponse:
    out: UpdateDependencyResponse = {}  # type: ignore[typeddict-item]
    if data.get("dependencyId") is not None:
        out["dependency_id"] = data["dependencyId"]
    else:
        out["dependency_id"] = ""
    if data.get("dependencyName") is not None:
        out["dependency_name"] = data["dependencyName"]
    else:
        out["dependency_name"] = ""
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        import typing

        out["criticality"] = typing.cast(
            "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality",
            "",
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
