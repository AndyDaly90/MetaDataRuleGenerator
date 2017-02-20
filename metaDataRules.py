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
               "[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[" \
               "-SEP-]][[-SEP-]][[-SEP-]]"
        return rule
