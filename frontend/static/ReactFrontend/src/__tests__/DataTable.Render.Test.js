import React from 'react';
import { render } from '@testing-library/react';
import CustomPaginationActionsTable from "../components/DataTable";

test('renders entire application', () => {
  const { getByText } = render(<CustomPaginationActionsTable />);
});