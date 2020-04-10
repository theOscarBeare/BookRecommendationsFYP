import React from 'react';
import { render } from '@testing-library/react';
import App from '../components/App';

test('renders entire application', () => {
  const { getByText } = render(<App />);
});
