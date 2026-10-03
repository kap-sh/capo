"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceChangeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.causing_entity
    import capo_cloudformation.types.change_source
    import capo_cloudformation.types.evaluation_type
    import capo_cloudformation.types.resource_target_definition


class ResourceChangeDetail(TypedDict, closed=True):
    target: NotRequired[
        "capo_cloudformation.types.resource_target_definition.ResourceTargetDefinition"
    ]
    """<p>A <code>ResourceTargetDefinition</code> structure that describes the field that CloudFormation will change and whether the resource will be recreated.</p>"""
    evaluation: NotRequired["capo_cloudformation.types.evaluation_type.EvaluationType"]
    """<p>Indicates whether CloudFormation can determine the target value, and whether the target value will change before you execute a change set.</p> <p>For <code>Static</code> evaluations, CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the <code>InstanceType</code> property of an EC2 instance, CloudFormation knows that this property value will change, and its value, so this is a <code>Static</code> evaluation.</p> <p>For <code>Dynamic</code> evaluations, can't determine the target value because it depends on the result of an intrinsic function, such as a <code>Ref</code> or <code>Fn::GetAtt</code> intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that's conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.</p>"""
    change_source: NotRequired["capo_cloudformation.types.change_source.ChangeSource"]
    """<p>The group to which the <code>CausingEntity</code> value belongs. There are five entity groups:</p> <ul> <li> <p> <code>ResourceReference</code> entities are <code>Ref</code> intrinsic functions that refer to resources in the template, such as <code>{ "Ref" : "MyEC2InstanceResource" }</code>.</p> </li> <li> <p> <code>ParameterReference</code> entities are <code>Ref</code> intrinsic functions that get template parameter values, such as <code>{ "Ref" : "MyPasswordParameter" }</code>.</p> </li> <li> <p> <code>ResourceAttribute</code> entities are <code>Fn::GetAtt</code> intrinsic functions that get resource attribute values, such as <code>{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }</code>.</p> </li> <li> <p> <code>DirectModification</code> entities are changes that are made directly to the template.</p> </li> <li> <p> <code>Automatic</code> entities are <code>AWS::CloudFormation::Stack</code> resource types, which are also known as nested stacks. If you made no changes to the <code>AWS::CloudFormation::Stack</code> resource, CloudFormation sets the <code>ChangeSource</code> to <code>Automatic</code> because the nested stack's template might have changed. Changes to a nested stack's template aren't visible to CloudFormation until you run an update on the parent stack.</p> </li> <li> <p> <code>NoModification</code> entities are changes made to the template that matches the actual state of the resource.</p> </li> </ul>"""
    causing_entity: NotRequired[
        "capo_cloudformation.types.causing_entity.CausingEntity"
    ]
    """<p>The identity of the entity that triggered this change. This entity is a member of the group that's specified by the <code>ChangeSource</code> field. For example, if you modified the value of the <code>KeyPairName</code> parameter, the <code>CausingEntity</code> is the name of the parameter (<code>KeyPairName</code>).</p> <p>If the <code>ChangeSource</code> value is <code>DirectModification</code>, no value is given for <code>CausingEntity</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceChangeDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target" in value:
        import capo_cloudformation.types.resource_target_definition

        capo_cloudformation.types.resource_target_definition.serialize_query(
            value["target"], pairs, f"{key_prefix}Target"
        )
    if "evaluation" in value:
        import capo_cloudformation.types.evaluation_type

        capo_cloudformation.types.evaluation_type.serialize_query(
            value["evaluation"], pairs, f"{key_prefix}Evaluation"
        )
    if "change_source" in value:
        import capo_cloudformation.types.change_source

        capo_cloudformation.types.change_source.serialize_query(
            value["change_source"], pairs, f"{key_prefix}ChangeSource"
        )
    if "causing_entity" in value:
        pairs.append((f"{key_prefix}CausingEntity", str(value["causing_entity"])))


def deserialize_query(el: Element) -> ResourceChangeDetail:
    out: ResourceChangeDetail = {}  # type: ignore[typeddict-item]
    child_target = el.find("Target")
    if child_target is not None:
        import capo_cloudformation.types.resource_target_definition

        out["target"] = (
            capo_cloudformation.types.resource_target_definition.deserialize_query(
                child_target
            )
        )
    child_evaluation = el.find("Evaluation")
    if child_evaluation is not None:
        import capo_cloudformation.types.evaluation_type

        out["evaluation"] = capo_cloudformation.types.evaluation_type.deserialize_query(
            child_evaluation
        )
    child_change_source = el.find("ChangeSource")
    if child_change_source is not None:
        import capo_cloudformation.types.change_source

        out["change_source"] = (
            capo_cloudformation.types.change_source.deserialize_query(
                child_change_source
            )
        )
    child_causing_entity = el.find("CausingEntity")
    if child_causing_entity is not None:
        out["causing_entity"] = str(child_causing_entity.text or "")
    return out
