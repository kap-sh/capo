"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DeleteTemplateGroupAccessControlEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.group_security_identifier
    import capo_pca_connector_ad.types.template_arn


class DeleteTemplateGroupAccessControlEntryRequest(TypedDict, closed=True):
    template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    group_security_identifier: (
        "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier"
    )
    """<p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateGroupAccessControlEntryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTemplateGroupAccessControlEntryRequest:
    out: DeleteTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
    return out
