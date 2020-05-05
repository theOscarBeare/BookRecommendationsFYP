import React from 'react';
import { render } from '@testing-library/react';
import recommendedBook from '../components/RecommendedBook';

test('renders the book recommendation page', () => {
  const { getByText } = render(<recommendedBook/>);
});
