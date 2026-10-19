"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageOriginRestrictions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.allow_publish
    import capo_codeartifact.types.allow_upstream


class PackageOriginRestrictions(TypedDict, closed=True):
    publish: "capo_codeartifact.types.allow_publish.AllowPublish"
    """<p>The package origin configuration that determines if new versions of the package can be published directly to the repository.</p>"""
    upstream: "capo_codeartifact.types.allow_upstream.AllowUpstream"
    """<p>The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageOriginRestrictions) -> dict:
    out: dict = {}
    import capo_codeartifact.types.allow_publish

    out["publish"] = capo_codeartifact.types.allow_publish.serialize_json(
        value["publish"]
    )
    import capo_codeartifact.types.allow_upstream

    out["upstream"] = capo_codeartifact.types.allow_upstream.serialize_json(
        value["upstream"]
    )
    return out


def deserialize_json(data: dict) -> PackageOriginRestrictions:
    out: PackageOriginRestrictions = {}  # type: ignore[typeddict-item]
    if data.get("publish") is not None:
        import capo_codeartifact.types.allow_publish

        out["publish"] = capo_codeartifact.types.allow_publish.deserialize_json(
            data["publish"]
        )
    else:
        import typing

        out["publish"] = typing.cast(
            "capo_codeartifact.types.allow_publish.AllowPublish", ""
        )
    if data.get("upstream") is not None:
        import capo_codeartifact.types.allow_upstream

        out["upstream"] = capo_codeartifact.types.allow_upstream.deserialize_json(
            data["upstream"]
        )
    else:
        import typing

        out["upstream"] = typing.cast(
            "capo_codeartifact.types.allow_upstream.AllowUpstream", ""
        )
    return out
