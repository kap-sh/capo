"""Generated from Smithy shape ``com.amazonaws.ses#SendCustomVerificationEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.configuration_set_name
    import capo_ses.types.template_name


class SendCustomVerificationEmailRequest(TypedDict, closed=True):
    email_address: "capo_ses.types.address.Address"
    """<p>The email address to verify.</p>"""
    template_name: "capo_ses.types.template_name.TemplateName"
    """<p>The name of the custom verification email template to use when sending the verification email.</p>"""
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>Name of a configuration set to use when sending the verification email.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendCustomVerificationEmailRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EmailAddress", str(value["email_address"])))
    pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "configuration_set_name" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
        )


def deserialize_query(el: Element) -> SendCustomVerificationEmailRequest:
    out: SendCustomVerificationEmailRequest = {}  # type: ignore[typeddict-item]
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    else:
        out["email_address"] = ""
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        out["template_name"] = ""
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    return out
