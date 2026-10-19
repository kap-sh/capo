"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#MaxAgeRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.boxed_boolean
    import capo_elastic_beanstalk.types.boxed_int


class MaxAgeRule(TypedDict, closed=True):
    enabled: "capo_elastic_beanstalk.types.boxed_boolean.BoxedBoolean"
    """<p>Specify <code>true</code> to apply the rule, or <code>false</code> to disable it.</p>"""
    max_age_in_days: NotRequired["capo_elastic_beanstalk.types.boxed_int.BoxedInt"]
    """<p>Specify the number of days to retain an application versions.</p>"""
    delete_source_from_s3: NotRequired[
        "capo_elastic_beanstalk.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Set to <code>true</code> to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MaxAgeRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "max_age_in_days" in value:
        pairs.append((f"{key_prefix}MaxAgeInDays", str(value["max_age_in_days"])))
    if "delete_source_from_s3" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteSourceFromS3",
                "true" if value["delete_source_from_s3"] else "false",
            )
        )


def deserialize_query(el: Element) -> MaxAgeRule:
    out: MaxAgeRule = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_max_age_in_days = el.find("MaxAgeInDays")
    if child_max_age_in_days is not None:
        out["max_age_in_days"] = int(child_max_age_in_days.text or "")
    child_delete_source_from_s3 = el.find("DeleteSourceFromS3")
    if child_delete_source_from_s3 is not None:
        out["delete_source_from_s3"] = (
            child_delete_source_from_s3.text or ""
        ).lower() == "true"
    return out
