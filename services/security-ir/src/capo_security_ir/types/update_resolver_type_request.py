"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateResolverTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.resolver_type


class UpdateResolverTypeRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateResolverType to identify the case to update.</p>"""
    resolver_type: "capo_security_ir.types.resolver_type.ResolverType"
    """<p>Required element for UpdateResolverType to identify the new resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResolverTypeRequest) -> dict:
    out: dict = {}
    import capo_security_ir.types.resolver_type

    out["resolverType"] = capo_security_ir.types.resolver_type.serialize_json(
        value["resolver_type"]
    )
    return out


def deserialize_json(data: dict) -> UpdateResolverTypeRequest:
    out: UpdateResolverTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("resolverType") is not None:
        import capo_security_ir.types.resolver_type

        out["resolver_type"] = capo_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    else:
        import typing

        out["resolver_type"] = typing.cast(
            "capo_security_ir.types.resolver_type.ResolverType", ""
        )
    return out
