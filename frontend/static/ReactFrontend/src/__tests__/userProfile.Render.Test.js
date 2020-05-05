import React from 'react';
import { render } from '@testing-library/react';
import userProfile from '../components/userProfile';

test('renders the user profile page', () => {
  const { getByText } = render(<userProfile/>);
});
