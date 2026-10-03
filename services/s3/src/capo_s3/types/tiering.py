"""Generated from Smithy shape ``com.amazonaws.s3#Tiering``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.intelligent_tiering_access_tier
    import capo_s3.types.intelligent_tiering_days


class Tiering(TypedDict, closed=True):
    days: "capo_s3.types.intelligent_tiering_days.IntelligentTieringDays"
    """<p>The number of consecutive days of no access after which an object will be eligible to be transitioned to the corresponding tier. The minimum number of days specified for Archive Access tier must be at least 90 days and Deep Archive Access tier must be at least 180 days. The maximum can be up to 2 years (730 days).</p>"""
    access_tier: (
        "capo_s3.types.intelligent_tiering_access_tier.IntelligentTieringAccessTier"
    )
    """<p>S3 Intelligent-Tiering access tier. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access">Storage class for automatically optimizing frequently and infrequently accessed objects</a> for a list of access tiers in the S3 Intelligent-Tiering storage class.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Tiering, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Days").text = str(value["days"])
    import capo_s3.types.intelligent_tiering_access_tier

    capo_s3.types.intelligent_tiering_access_tier.serialize_xml(
        value["access_tier"], el, "AccessTier"
    )


def deserialize_xml(el: Element) -> Tiering:
    out: Tiering = {}  # type: ignore[typeddict-item]
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    else:
        raise DeserializationError("Tiering.days required")
    child_access_tier = el.find("AccessTier")
    if child_access_tier is not None:
        import capo_s3.types.intelligent_tiering_access_tier

        out["access_tier"] = (
            capo_s3.types.intelligent_tiering_access_tier.deserialize_xml(
                child_access_tier
            )
        )
    else:
        raise DeserializationError("Tiering.access_tier required")
    return out
