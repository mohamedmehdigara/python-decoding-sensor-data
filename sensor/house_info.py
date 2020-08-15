class HouseInfo{
    def __init__(self, data){
        self.data = data
    }
    get_data_by_Area(self, field, rec_area=0){
        field_data = []
        for record in self.data:
            if (rec_area = 0):
                record[field].append(field_data)
            elif (rec_area = record['area']):
                record[field].append(field_data)
        return field_data


    }
}