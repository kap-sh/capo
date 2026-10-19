"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GetControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_controlcatalog.types.control_aliases
    import capo_controlcatalog.types.control_arn
    import capo_controlcatalog.types.control_behavior
    import capo_controlcatalog.types.control_parameters
    import capo_controlcatalog.types.control_severity
    import capo_controlcatalog.types.governed_providers
    import capo_controlcatalog.types.governed_resources
    import capo_controlcatalog.types.implementation_details
    import capo_controlcatalog.types.parameter_requirement_summary
    import capo_controlcatalog.types.region_configuration


class GetControlResponse(TypedDict, closed=True):
    arn: "capo_controlcatalog.types.control_arn.ControlArn"
    """<p>The Amazon Resource Name (ARN) of the control.</p>"""
    aliases: NotRequired["capo_controlcatalog.types.control_aliases.ControlAliases"]
    """<p>A list of alternative identifiers for the control. These are human-readable designators, such as <code>SH.S3.1</code>. Several aliases can refer to the same control across different Amazon Web Services services or compliance frameworks.</p>"""
    name: "str"
    """<p>The display name of the control.</p>"""
    description: "str"
    """<p>A description of what the control does.</p>"""
    behavior: "capo_controlcatalog.types.control_behavior.ControlBehavior"
    """<p>A term that identifies the control's functional behavior. One of <code>Preventive</code>, <code>Detective</code>, <code>Proactive</code> </p>"""
    severity: NotRequired["capo_controlcatalog.types.control_severity.ControlSeverity"]
    """<p>An enumerated type, with the following possible values:</p>"""
    region_configuration: (
        "capo_controlcatalog.types.region_configuration.RegionConfiguration"
    )
    implementation: NotRequired[
        "capo_controlcatalog.types.implementation_details.ImplementationDetails"
    ]
    """<p>Returns information about the control, as an <code>ImplementationDetails</code> object that shows the underlying implementation type for a control.</p>"""
    parameter_requirement_summary: NotRequired[
        "capo_controlcatalog.types.parameter_requirement_summary.ParameterRequirementSummary"
    ]
    """<p>A summary that indicates whether the control requires parameters, accepts optional parameters, or does not support parameters. Use this field to determine whether you need to supply parameter values when you enable the control.</p>"""
    parameters: NotRequired[
        "capo_controlcatalog.types.control_parameters.ControlParameters"
    ]
    """<p>Returns an array of <code>ControlParameter</code> objects that specify the parameters a control supports. An empty list is returned for controls that don’t support parameters. </p>"""
    create_time: NotRequired["datetime.datetime"]
    """<p>A timestamp that notes the time when the control was released (start of its life) as a governance capability in Amazon Web Services.</p>"""
    governed_resources: NotRequired[
        "capo_controlcatalog.types.governed_resources.GovernedResources"
    ]
    """<p>A list of resource types that are governed by this control. This information helps you understand which controls can govern certain types of resources, and conversely, which resources are affected when the control is implemented. For Amazon Web Services controls, the resources are represented as CloudFormation resource types. For non-Amazon Web Services controls, the resources are represented in a provider-specific format. If <code>GovernedResources</code> cannot be represented by available resource types, it’s returned as an empty list.</p>"""
    governed_providers: NotRequired[
        "capo_controlcatalog.types.governed_providers.GovernedProviders"
    ]
    """<p>A list of providers whose resources are governed by this control. For example, a value of <code>AWS</code> indicates that the control governs Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "aliases" in value:
        import capo_controlcatalog.types.control_aliases

        out["Aliases"] = capo_controlcatalog.types.control_aliases.serialize_json(
            value["aliases"]
        )
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_controlcatalog.types.control_behavior

    out["Behavior"] = capo_controlcatalog.types.control_behavior.serialize_json(
        value["behavior"]
    )
    if "severity" in value:
        import capo_controlcatalog.types.control_severity

        out["Severity"] = capo_controlcatalog.types.control_severity.serialize_json(
            value["severity"]
        )
    import capo_controlcatalog.types.region_configuration

    out["RegionConfiguration"] = (
        capo_controlcatalog.types.region_configuration.serialize_json(
            value["region_configuration"]
        )
    )
    if "implementation" in value:
        import capo_controlcatalog.types.implementation_details

        out["Implementation"] = (
            capo_controlcatalog.types.implementation_details.serialize_json(
                value["implementation"]
            )
        )
    if "parameter_requirement_summary" in value:
        import capo_controlcatalog.types.parameter_requirement_summary

        out["ParameterRequirementSummary"] = (
            capo_controlcatalog.types.parameter_requirement_summary.serialize_json(
                value["parameter_requirement_summary"]
            )
        )
    if "parameters" in value:
        import capo_controlcatalog.types.control_parameters

        out["Parameters"] = capo_controlcatalog.types.control_parameters.serialize_json(
            value["parameters"]
        )
    if "create_time" in value:
        import capo_controlcatalog.types._prelude.timestamp

        out["CreateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
            value["create_time"]
        )
    if "governed_resources" in value:
        import capo_controlcatalog.types.governed_resources

        out["GovernedResources"] = (
            capo_controlcatalog.types.governed_resources.serialize_json(
                value["governed_resources"]
            )
        )
    if "governed_providers" in value:
        import capo_controlcatalog.types.governed_providers

        out["GovernedProviders"] = (
            capo_controlcatalog.types.governed_providers.serialize_json(
                value["governed_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetControlResponse:
    out: GetControlResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Aliases") is not None:
        import capo_controlcatalog.types.control_aliases

        out["aliases"] = capo_controlcatalog.types.control_aliases.deserialize_json(
            data["Aliases"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Behavior") is not None:
        import capo_controlcatalog.types.control_behavior

        out["behavior"] = capo_controlcatalog.types.control_behavior.deserialize_json(
            data["Behavior"]
        )
    else:
        import typing

        out["behavior"] = typing.cast(
            "capo_controlcatalog.types.control_behavior.ControlBehavior", ""
        )
    if data.get("Severity") is not None:
        import capo_controlcatalog.types.control_severity

        out["severity"] = capo_controlcatalog.types.control_severity.deserialize_json(
            data["Severity"]
        )
    if data.get("RegionConfiguration") is not None:
        import capo_controlcatalog.types.region_configuration

        out["region_configuration"] = (
            capo_controlcatalog.types.region_configuration.deserialize_json(
                data["RegionConfiguration"]
            )
        )
    else:
        raise DeserializationError("GetControlResponse.region_configuration required")
    if data.get("Implementation") is not None:
        import capo_controlcatalog.types.implementation_details

        out["implementation"] = (
            capo_controlcatalog.types.implementation_details.deserialize_json(
                data["Implementation"]
            )
        )
    if data.get("ParameterRequirementSummary") is not None:
        import capo_controlcatalog.types.parameter_requirement_summary

        out["parameter_requirement_summary"] = (
            capo_controlcatalog.types.parameter_requirement_summary.deserialize_json(
                data["ParameterRequirementSummary"]
            )
        )
    if data.get("Parameters") is not None:
        import capo_controlcatalog.types.control_parameters

        out["parameters"] = (
            capo_controlcatalog.types.control_parameters.deserialize_json(
                data["Parameters"]
            )
        )
    if data.get("CreateTime") is not None:
        import capo_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            capo_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    if data.get("GovernedResources") is not None:
        import capo_controlcatalog.types.governed_resources

        out["governed_resources"] = (
            capo_controlcatalog.types.governed_resources.deserialize_json(
                data["GovernedResources"]
            )
        )
    if data.get("GovernedProviders") is not None:
        import capo_controlcatalog.types.governed_providers

        out["governed_providers"] = (
            capo_controlcatalog.types.governed_providers.deserialize_json(
                data["GovernedProviders"]
            )
        )
    return out
