import React from 'react';
import { render } from '@testing-library/react';
import randomBook from '../components/randomBook';

test('renders the random book page', () => {
  const { getByText } = render(<randomBook/>);
});
