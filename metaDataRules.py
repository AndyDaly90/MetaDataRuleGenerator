class MetaDataRules:
    def __init__(self):
        pass

    @staticmethod
    def setValue(form_id, dest_field_id, set_val):
        rule = "SetValue[[-SEP-]]" + str(form_id) + "[[-SEP-]]" \
               + str(dest_field_id) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]][[-SEP-]]" \
               + str(set_val) + "[[-SEP-]][[" \
                                "-SEP-]][[" \
                                "-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def concat(form_id, dest_field_id, first_field_id, concat_value, second_field_id):
        rule = "Concat[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(dest_field_id) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(first_field_id) + "[[-SEP-]][[-SEP-]]" \
               + str(form_id) + "[[-SEP-]][[-SEP-]]" \
               + str(concat_value) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(second_field_id) + "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def stringToDate(destination_field_id, source_field_id):
        rule = "NumberStringToDate[[-SEP-]]" \
               + str(destination_field_id) + "[[-SEP-]]" \
               + str(source_field_id) + "[[-SEP-]]True[[-SEP-]][" \
                                        "[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[" \
                                        "-SEP-]][[-SEP-]][[" \
                                        "-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def crossDbInsert(source_id, source_form, source_field_values,
                      destination_id, destination_field_values):
        source_str = ""
        dest_str = ""

        for i in range(len(source_field_values)):
            if i == len(source_field_values)-1:
                source_str += source_field_values[i]
            else:
                source_str += source_field_values[i] + ","

        for i in range(len(destination_field_values)):
            if i == len(destination_field_values)-1:
                dest_str += destination_field_values[i]
            else:
                dest_str += destination_field_values[i] + ","

        rule = "CrossDatabase_Insert" \
               "[[-SEP-]]SOURCE_FORM_ID" \
               "[[-SEP-]]SOURCE_FORM" \
               "[[-SEP-]]SOURCE_FORM_ID" \
               "[[-SEP-]]SOURCE_FIELD_VALUES" \
               "[[-SEP-]]" \
               "[[-SEP-]]DEST_FORM_ID" \
               "[[-SEP-]]DESTINATION_FIELD_VALUES" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"

        rule = rule.replace("SOURCE_FORM_ID", source_id) \
            .replace("SOURCE_FORM", source_form) \
            .replace("SOURCE_FIELD_VALUES", source_str) \
            .replace("DEST_FORM_ID", destination_id) \
            .replace("DESTINATION_FIELD_VALUES", dest_str)
        return rule
