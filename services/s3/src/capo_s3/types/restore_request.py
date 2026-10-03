"""Generated from Smithy shape ``com.amazonaws.s3#RestoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.days
    import capo_s3.types.description
    import capo_s3.types.glacier_job_parameters
    import capo_s3.types.output_location
    import capo_s3.types.restore_request_type
    import capo_s3.types.select_parameters
    import capo_s3.types.tier


class RestoreRequest(TypedDict, closed=True):
    days: NotRequired["capo_s3.types.days.Days"]
    """<p>Lifetime of the active copy in days. Do not use with restores that specify <code>OutputLocation</code>.</p> <p>The Days element is required for regular restores, and must not be provided for select requests.</p>"""
    glacier_job_parameters: NotRequired[
        "capo_s3.types.glacier_job_parameters.GlacierJobParameters"
    ]
    """<p>S3 Glacier related parameters pertaining to this job. Do not use with restores that specify <code>OutputLocation</code>.</p>"""
    type: NotRequired["capo_s3.types.restore_request_type.RestoreRequestType"]
    """<important> <p>Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. <a href="http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/">Learn more</a> </p> </important> <p>Type of restore request.</p>"""
    tier: NotRequired["capo_s3.types.tier.Tier"]
    """<p>Retrieval tier at which the restore will be processed.</p>"""
    description: NotRequired["capo_s3.types.description.Description"]
    """<p>The optional description for the job.</p>"""
    select_parameters: NotRequired["capo_s3.types.select_parameters.SelectParameters"]
    """<important> <p>Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. <a href="http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/">Learn more</a> </p> </important> <p>Describes the parameters for Select job types.</p>"""
    output_location: NotRequired["capo_s3.types.output_location.OutputLocation"]
    """<p>Describes the location where the restore job's output is stored.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RestoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "glacier_job_parameters" in value:
        import capo_s3.types.glacier_job_parameters

        capo_s3.types.glacier_job_parameters.serialize_xml(
            value["glacier_job_parameters"], el, "GlacierJobParameters"
        )
    if "type" in value:
        import capo_s3.types.restore_request_type

        capo_s3.types.restore_request_type.serialize_xml(value["type"], el, "Type")
    if "tier" in value:
        import capo_s3.types.tier

        capo_s3.types.tier.serialize_xml(value["tier"], el, "Tier")
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])
    if "select_parameters" in value:
        import capo_s3.types.select_parameters

        capo_s3.types.select_parameters.serialize_xml(
            value["select_parameters"], el, "SelectParameters"
        )
    if "output_location" in value:
        import capo_s3.types.output_location

        capo_s3.types.output_location.serialize_xml(
            value["output_location"], el, "OutputLocation"
        )


def deserialize_xml(el: Element) -> RestoreRequest:
    out: RestoreRequest = {}  # type: ignore[typeddict-item]
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_glacier_job_parameters = el.find("GlacierJobParameters")
    if child_glacier_job_parameters is not None:
        import capo_s3.types.glacier_job_parameters

        out["glacier_job_parameters"] = (
            capo_s3.types.glacier_job_parameters.deserialize_xml(
                child_glacier_job_parameters
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import capo_s3.types.restore_request_type

        out["type"] = capo_s3.types.restore_request_type.deserialize_xml(child_type)
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_s3.types.tier

        out["tier"] = capo_s3.types.tier.deserialize_xml(child_tier)
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_select_parameters = el.find("SelectParameters")
    if child_select_parameters is not None:
        import capo_s3.types.select_parameters

        out["select_parameters"] = capo_s3.types.select_parameters.deserialize_xml(
            child_select_parameters
        )
    child_output_location = el.find("OutputLocation")
    if child_output_location is not None:
        import capo_s3.types.output_location

        out["output_location"] = capo_s3.types.output_location.deserialize_xml(
            child_output_location
        )
    return out
