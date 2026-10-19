"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_designation
    import capo_datazone.types.domain_unit_grant_filter
    import capo_datazone.types.domain_unit_id


class DomainUnitPolicyGrantPrincipal(TypedDict, closed=True):
    domain_unit_designation: (
        "capo_datazone.types.domain_unit_designation.DomainUnitDesignation"
    )
    """<p>Specifes the designation of the domain unit users.</p>"""
    domain_unit_identifier: NotRequired[
        "capo_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the domain unit.</p>"""
    domain_unit_grant_filter: NotRequired[
        "capo_datazone.types.domain_unit_grant_filter.DomainUnitGrantFilter"
    ]
    """<p>The grant filter for the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitPolicyGrantPrincipal) -> dict:
    out: dict = {}
    import capo_datazone.types.domain_unit_designation

    out["domainUnitDesignation"] = (
        capo_datazone.types.domain_unit_designation.serialize_json(
            value["domain_unit_designation"]
        )
    )
    if "domain_unit_identifier" in value:
        out["domainUnitIdentifier"] = value["domain_unit_identifier"]
    if "domain_unit_grant_filter" in value:
        import capo_datazone.types.domain_unit_grant_filter

        out["domainUnitGrantFilter"] = (
            capo_datazone.types.domain_unit_grant_filter.serialize_json(
                value["domain_unit_grant_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainUnitPolicyGrantPrincipal:
    out: DomainUnitPolicyGrantPrincipal = {}  # type: ignore[typeddict-item]
    if data.get("domainUnitDesignation") is not None:
        import capo_datazone.types.domain_unit_designation

        out["domain_unit_designation"] = (
            capo_datazone.types.domain_unit_designation.deserialize_json(
                data["domainUnitDesignation"]
            )
        )
    else:
        import typing

        out["domain_unit_designation"] = typing.cast(
            "capo_datazone.types.domain_unit_designation.DomainUnitDesignation", ""
        )
    if data.get("domainUnitIdentifier") is not None:
        out["domain_unit_identifier"] = data["domainUnitIdentifier"]
    if data.get("domainUnitGrantFilter") is not None:
        import capo_datazone.types.domain_unit_grant_filter

        out["domain_unit_grant_filter"] = (
            capo_datazone.types.domain_unit_grant_filter.deserialize_json(
                data["domainUnitGrantFilter"]
            )
        )
    return out
