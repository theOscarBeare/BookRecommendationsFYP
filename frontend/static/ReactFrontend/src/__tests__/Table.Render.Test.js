import React from 'react';
import { render } from '@testing-library/react';
import Table from '../components/Table';


// This test creates a table and used the const test as its data provider

test('renders entire application', () => {
    const Test = "test";
    const { getByText } = render(<Table  data={Test}/>);
});
