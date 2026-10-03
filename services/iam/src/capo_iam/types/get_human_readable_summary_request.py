"""Generated from Smithy shape ``com.amazonaws.iam#GetHumanReadableSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.locale_type


class GetHumanReadableSummaryRequest(TypedDict, closed=True):
    entity_arn: "capo_iam.types.arn_type.arnType"
    """<p>Arn of the entity to be summarized. At this time, the only supported entity type is <code>delegation-request</code> </p>"""
    locale: NotRequired["capo_iam.types.locale_type.localeType"]
    """<p>A string representing the locale to use for the summary generation. The supported locale strings are based on the <a href="/awsconsolehelpdocs/latest/gsg/change-language.html#supported-languages"> Supported languages of the Amazon Web Services Management Console </a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetHumanReadableSummaryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EntityArn", str(value["entity_arn"])))
    if "locale" in value:
        pairs.append((f"{key_prefix}Locale", str(value["locale"])))


def deserialize_query(el: Element) -> GetHumanReadableSummaryRequest:
    out: GetHumanReadableSummaryRequest = {}  # type: ignore[typeddict-item]
    child_entity_arn = el.find("EntityArn")
    if child_entity_arn is not None:
        out["entity_arn"] = str(child_entity_arn.text or "")
    else:
        raise DeserializationError("GetHumanReadableSummaryRequest.entity_arn required")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    return out
