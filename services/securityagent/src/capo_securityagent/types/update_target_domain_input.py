"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateTargetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.domain_verification_method
    import capo_securityagent.types.target_domain_id


class UpdateTargetDomainInput(TypedDict, closed=True):
    target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain to update.</p>"""
    verification_method: (
        "capo_securityagent.types.domain_verification_method.DomainVerificationMethod"
    )
    """<p>The updated verification method for the target domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    import capo_securityagent.types.domain_verification_method

    out["verificationMethod"] = (
        capo_securityagent.types.domain_verification_method.serialize_json(
            value["verification_method"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTargetDomainInput:
    out: UpdateTargetDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainId") is not None:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        out["target_domain_id"] = ""
    if data.get("verificationMethod") is not None:
        import capo_securityagent.types.domain_verification_method

        out["verification_method"] = (
            capo_securityagent.types.domain_verification_method.deserialize_json(
                data["verificationMethod"]
            )
        )
    else:
        import typing

        out["verification_method"] = typing.cast(
            "capo_securityagent.types.domain_verification_method.DomainVerificationMethod",
            "",
        )
    return out
