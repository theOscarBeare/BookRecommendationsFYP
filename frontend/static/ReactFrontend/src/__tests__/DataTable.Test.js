import React from "react";
import CustomPaginationActionsTable from "../components/DataTable";


function table(props) {
    return <CustomPaginationActionsTable/>
    
}
describe("Data Table", () => {
  test("Matches the data table", () => {
    const table = create(<CustomPaginationActionsTable />);
    expect(table.toJSON()).toMatchSnapshot();
  });
});