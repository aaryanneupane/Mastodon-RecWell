import React from 'react';

interface ImageViewerProps {
  imageUrl: string;
  onClose: () => void;
}

const ImageViewer: React.FC<ImageViewerProps> = ({ imageUrl, onClose }) => {
  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50"
      onClick={onClose} 
    >
      <button
        className="absolute top-5 right-5 text-white text-3xl font-bold z-50"
        onClick={(e) => {
          e.stopPropagation(); 
          onClose();
        }}
      >
        &times;
      </button>
      
      <div className="relative p-4">
        <img
          src={imageUrl}
          alt="Enlarged view"
          className="max-w-full max-h-[85vh] rounded-lg"
          onClick={(e) => e.stopPropagation()} 
        />
      </div>
    </div>
  );
};

export default ImageViewer;