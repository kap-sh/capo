"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleAction``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.add_header_action
    import capo_mailmanager.types.archive_action
    import capo_mailmanager.types.bounce_action
    import capo_mailmanager.types.deliver_to_mailbox_action
    import capo_mailmanager.types.deliver_to_q_business_action
    import capo_mailmanager.types.drop_action
    import capo_mailmanager.types.invoke_lambda_action
    import capo_mailmanager.types.relay_action
    import capo_mailmanager.types.replace_recipient_action
    import capo_mailmanager.types.s3_action
    import capo_mailmanager.types.send_action
    import capo_mailmanager.types.sns_action


class RuleActionDropMember(TypedDict, closed=True):
    Drop: "capo_mailmanager.types.drop_action.DropAction"


class RuleActionRelayMember(TypedDict, closed=True):
    Relay: "capo_mailmanager.types.relay_action.RelayAction"


class RuleActionArchiveMember(TypedDict, closed=True):
    Archive: "capo_mailmanager.types.archive_action.ArchiveAction"


class RuleActionWriteToS3Member(TypedDict, closed=True):
    WriteToS3: "capo_mailmanager.types.s3_action.S3Action"


class RuleActionSendMember(TypedDict, closed=True):
    Send: "capo_mailmanager.types.send_action.SendAction"


class RuleActionAddHeaderMember(TypedDict, closed=True):
    AddHeader: "capo_mailmanager.types.add_header_action.AddHeaderAction"


class RuleActionReplaceRecipientMember(TypedDict, closed=True):
    ReplaceRecipient: (
        "capo_mailmanager.types.replace_recipient_action.ReplaceRecipientAction"
    )


class RuleActionDeliverToMailboxMember(TypedDict, closed=True):
    DeliverToMailbox: (
        "capo_mailmanager.types.deliver_to_mailbox_action.DeliverToMailboxAction"
    )


class RuleActionDeliverToQBusinessMember(TypedDict, closed=True):
    DeliverToQBusiness: (
        "capo_mailmanager.types.deliver_to_q_business_action.DeliverToQBusinessAction"
    )


class RuleActionPublishToSnsMember(TypedDict, closed=True):
    PublishToSns: "capo_mailmanager.types.sns_action.SnsAction"


class RuleActionBounceMember(TypedDict, closed=True):
    Bounce: "capo_mailmanager.types.bounce_action.BounceAction"


class RuleActionInvokeLambdaMember(TypedDict, closed=True):
    InvokeLambda: "capo_mailmanager.types.invoke_lambda_action.InvokeLambdaAction"


RuleAction: TypeAlias = (
    RuleActionDropMember
    | RuleActionRelayMember
    | RuleActionArchiveMember
    | RuleActionWriteToS3Member
    | RuleActionSendMember
    | RuleActionAddHeaderMember
    | RuleActionReplaceRecipientMember
    | RuleActionDeliverToMailboxMember
    | RuleActionDeliverToQBusinessMember
    | RuleActionPublishToSnsMember
    | RuleActionBounceMember
    | RuleActionInvokeLambdaMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Drop" in value:
        import capo_mailmanager.types.drop_action

        return {
            "Drop": capo_mailmanager.types.drop_action.serialize_aws_json_1_0(
                value["Drop"]
            )
        }
    elif "Relay" in value:
        import capo_mailmanager.types.relay_action

        return {
            "Relay": capo_mailmanager.types.relay_action.serialize_aws_json_1_0(
                value["Relay"]
            )
        }
    elif "Archive" in value:
        import capo_mailmanager.types.archive_action

        return {
            "Archive": capo_mailmanager.types.archive_action.serialize_aws_json_1_0(
                value["Archive"]
            )
        }
    elif "WriteToS3" in value:
        import capo_mailmanager.types.s3_action

        return {
            "WriteToS3": capo_mailmanager.types.s3_action.serialize_aws_json_1_0(
                value["WriteToS3"]
            )
        }
    elif "Send" in value:
        import capo_mailmanager.types.send_action

        return {
            "Send": capo_mailmanager.types.send_action.serialize_aws_json_1_0(
                value["Send"]
            )
        }
    elif "AddHeader" in value:
        import capo_mailmanager.types.add_header_action

        return {
            "AddHeader": capo_mailmanager.types.add_header_action.serialize_aws_json_1_0(
                value["AddHeader"]
            )
        }
    elif "ReplaceRecipient" in value:
        import capo_mailmanager.types.replace_recipient_action

        return {
            "ReplaceRecipient": capo_mailmanager.types.replace_recipient_action.serialize_aws_json_1_0(
                value["ReplaceRecipient"]
            )
        }
    elif "DeliverToMailbox" in value:
        import capo_mailmanager.types.deliver_to_mailbox_action

        return {
            "DeliverToMailbox": capo_mailmanager.types.deliver_to_mailbox_action.serialize_aws_json_1_0(
                value["DeliverToMailbox"]
            )
        }
    elif "DeliverToQBusiness" in value:
        import capo_mailmanager.types.deliver_to_q_business_action

        return {
            "DeliverToQBusiness": capo_mailmanager.types.deliver_to_q_business_action.serialize_aws_json_1_0(
                value["DeliverToQBusiness"]
            )
        }
    elif "PublishToSns" in value:
        import capo_mailmanager.types.sns_action

        return {
            "PublishToSns": capo_mailmanager.types.sns_action.serialize_aws_json_1_0(
                value["PublishToSns"]
            )
        }
    elif "Bounce" in value:
        import capo_mailmanager.types.bounce_action

        return {
            "Bounce": capo_mailmanager.types.bounce_action.serialize_aws_json_1_0(
                value["Bounce"]
            )
        }
    elif "InvokeLambda" in value:
        import capo_mailmanager.types.invoke_lambda_action

        return {
            "InvokeLambda": capo_mailmanager.types.invoke_lambda_action.serialize_aws_json_1_0(
                value["InvokeLambda"]
            )
        }
    else:
        raise SerializationError("RuleAction: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleAction:
    if data.get("Drop") is not None:
        import capo_mailmanager.types.drop_action

        return {
            "Drop": capo_mailmanager.types.drop_action.deserialize_aws_json_1_0(
                data["Drop"]
            )
        }
    elif data.get("Relay") is not None:
        import capo_mailmanager.types.relay_action

        return {
            "Relay": capo_mailmanager.types.relay_action.deserialize_aws_json_1_0(
                data["Relay"]
            )
        }
    elif data.get("Archive") is not None:
        import capo_mailmanager.types.archive_action

        return {
            "Archive": capo_mailmanager.types.archive_action.deserialize_aws_json_1_0(
                data["Archive"]
            )
        }
    elif data.get("WriteToS3") is not None:
        import capo_mailmanager.types.s3_action

        return {
            "WriteToS3": capo_mailmanager.types.s3_action.deserialize_aws_json_1_0(
                data["WriteToS3"]
            )
        }
    elif data.get("Send") is not None:
        import capo_mailmanager.types.send_action

        return {
            "Send": capo_mailmanager.types.send_action.deserialize_aws_json_1_0(
                data["Send"]
            )
        }
    elif data.get("AddHeader") is not None:
        import capo_mailmanager.types.add_header_action

        return {
            "AddHeader": capo_mailmanager.types.add_header_action.deserialize_aws_json_1_0(
                data["AddHeader"]
            )
        }
    elif data.get("ReplaceRecipient") is not None:
        import capo_mailmanager.types.replace_recipient_action

        return {
            "ReplaceRecipient": capo_mailmanager.types.replace_recipient_action.deserialize_aws_json_1_0(
                data["ReplaceRecipient"]
            )
        }
    elif data.get("DeliverToMailbox") is not None:
        import capo_mailmanager.types.deliver_to_mailbox_action

        return {
            "DeliverToMailbox": capo_mailmanager.types.deliver_to_mailbox_action.deserialize_aws_json_1_0(
                data["DeliverToMailbox"]
            )
        }
    elif data.get("DeliverToQBusiness") is not None:
        import capo_mailmanager.types.deliver_to_q_business_action

        return {
            "DeliverToQBusiness": capo_mailmanager.types.deliver_to_q_business_action.deserialize_aws_json_1_0(
                data["DeliverToQBusiness"]
            )
        }
    elif data.get("PublishToSns") is not None:
        import capo_mailmanager.types.sns_action

        return {
            "PublishToSns": capo_mailmanager.types.sns_action.deserialize_aws_json_1_0(
                data["PublishToSns"]
            )
        }
    elif data.get("Bounce") is not None:
        import capo_mailmanager.types.bounce_action

        return {
            "Bounce": capo_mailmanager.types.bounce_action.deserialize_aws_json_1_0(
                data["Bounce"]
            )
        }
    elif data.get("InvokeLambda") is not None:
        import capo_mailmanager.types.invoke_lambda_action

        return {
            "InvokeLambda": capo_mailmanager.types.invoke_lambda_action.deserialize_aws_json_1_0(
                data["InvokeLambda"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleAction: no recognized variant key")


def redact_sensitive(value: RuleAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ReplaceRecipient" in value:
        import capo_mailmanager.types.replace_recipient_action

        out["ReplaceRecipient"] = (
            capo_mailmanager.types.replace_recipient_action.redact_sensitive(
                value["ReplaceRecipient"]
            )
        )
    if "Bounce" in value:
        import capo_mailmanager.types.bounce_action

        out["Bounce"] = capo_mailmanager.types.bounce_action.redact_sensitive(
            value["Bounce"]
        )
    return out
